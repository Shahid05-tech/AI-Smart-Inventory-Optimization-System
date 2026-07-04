import  motion  from "framer-motion";

interface Props {
    children: React.ReactNode;
}

export default function AnimatedContainer({
    children,
}: Props) {
    return (
        <motion.div
            initial={{
                opacity: 0,
                y: 20,
            }}
            animate={{
                opacity: 1,
                y: 0,
            }}
            transition={{
                duration: 0.45,
            }}
        >
            {children}
        </motion.div>
    );
}